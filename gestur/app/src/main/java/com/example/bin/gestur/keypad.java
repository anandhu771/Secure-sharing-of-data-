package com.example.bin.gestur;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Handler;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.GridView;
import android.widget.Toast;

public class keypad extends AppCompatActivity {
GridView gv;
    char[] a;
        String[] data;


        Runnable rn=new Runnable() {
            @Override
            public void run() {

                Intent ins=new Intent(getApplicationContext(),app_login.class);
                startActivity(ins);
            }
        };

        Handler hnd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_keypad);
        gv=(GridView)findViewById(R.id.gview);
        SharedPreferences sh2= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String da=sh2.getString("data","");
        Toast.makeText(getApplicationContext(),"ddddddddddd"+da+"",Toast.LENGTH_SHORT).show();


        data=da.split("\\#");
//        data=new String[a.length];
//        for (int i=0;i<=a.length;i++) {
//            data[i] = String.valueOf(a[i]);
//        }
        Toast.makeText(getApplicationContext(),"data"+data+"",Toast.LENGTH_SHORT).show();
//        ArrayAdapter ad=new ArrayAdapter(this,android.R.layout.simple_list_item_1,data);
        gv.setAdapter(new Custom_keys(getApplicationContext(),data));

        hnd=new Handler();
        hnd.postDelayed(rn,50000);




    }
}
