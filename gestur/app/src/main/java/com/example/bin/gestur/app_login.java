package com.example.bin.gestur;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.preference.PreferenceManager;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class app_login extends Activity implements View.OnClickListener {
    Button b1,b2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_app_login);
        b1=(Button)findViewById(R.id.bqr);
        // b2=(Button)findViewById(R.id.bu4);
        b1.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        scanQR(v);

    }
    static final String ACTION_SCAN = "com.google.zxing.client.android.SCAN";
    public void scanQR(View v) {
        try {

            Intent intent = new Intent(ACTION_SCAN);
            intent.putExtra("SCAN_MODE", "QR_CODE_MODE");
            startActivityForResult(intent, 0);
        } catch (ActivityNotFoundException anfe) {
            showDialog(app_login.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
        }
    }
    private static AlertDialog   showDialog(final Activity act,CharSequence title,CharSequence message,CharSequence buttonYes,CharSequence buttonNo) {
        AlertDialog.Builder downloadDialog = new AlertDialog.Builder(act);
        downloadDialog.setTitle(title);
        downloadDialog.setMessage(message);
        downloadDialog.setPositiveButton(buttonYes, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialogInterface, int i) {
                Uri uri = Uri.parse("market://search?q=pname:" + "com.google.zxing.client.android");
                Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                try {
                    act.startActivity(intent);
                } catch (ActivityNotFoundException anfe) {

                }
            }
        });
        downloadDialog.setNegativeButton(buttonNo, new DialogInterface.OnClickListener() {
            public void onClick(DialogInterface dialogInterface, int i) {
            }
        });
        return downloadDialog.show();
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 0) {
            if (resultCode == RESULT_OK) {
                String contents = data.getStringExtra("SCAN_RESULT");
                String format = data.getStringExtra("SCAN_RESULT_FORMAT");






                SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                SharedPreferences.Editor ed=sh.edit();

                final String encryptdata=contents;

                TelephonyManager tm=(TelephonyManager)getSystemService(getApplicationContext().TELEPHONY_SERVICE);
                final String ime;
                if(ActivityCompat.checkSelfPermission(this, Manifest.permission.READ_PHONE_STATE)!= PackageManager.PERMISSION_GRANTED) {
                    return;
                }
                ime = "356786103846261"+"0";
                Toast.makeText(this,"imeiiiii"+ime+"",Toast.LENGTH_SHORT).show();

                Crypt enc=new Crypt(ime);
                try {

                    String decAns = new String(enc.decrypt_string(encryptdata));

                    Toast.makeText(this,"de__data====="+decAns,Toast.LENGTH_SHORT).show();


                    SharedPreferences sh2=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    SharedPreferences.Editor ed2=sh2.edit();
                    ed2.putString("data",decAns);
                    ed2.commit();

                    Intent i=new Intent(getApplicationContext(),keypad.class);
                    startActivity(i);
                } catch (Exception e) {
                    e.printStackTrace();
                    Log.d("error=============",e.getMessage());
                    Toast.makeText(this,"access denied",Toast.LENGTH_SHORT).show();



                }





            }
        }





    }
}
