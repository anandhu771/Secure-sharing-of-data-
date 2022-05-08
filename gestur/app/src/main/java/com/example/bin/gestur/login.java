package com.example.bin.gestur;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Display;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

public class login extends AppCompatActivity implements View.OnTouchListener, View.OnClickListener {
    ImageView imageView;
    Bitmap bitmap;
    Canvas canvas;
    Paint paint;
    Button saveB;
    String pattern;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String pp=sh.getString("pattern","");

        Toast.makeText(this,pp,Toast.LENGTH_SHORT).show();
        if(pp.equalsIgnoreCase(""))
        {
            Intent i=new Intent(getApplicationContext(),Registration.class);
            startActivity(i);
        }
        else {


            imageView = (ImageView) findViewById(R.id.ImageView);
            saveB = (Button) findViewById(R.id.login);

            saveB.setOnClickListener(this);

            Display currentDisplay = getWindowManager().getDefaultDisplay();
            float dw = currentDisplay.getWidth();
            float dh = currentDisplay.getHeight();

            bitmap = Bitmap.createBitmap((int) dw,(int) dh,
                    Bitmap.Config.ARGB_8888);
            canvas = new Canvas(bitmap);
            paint = new Paint();
            paint.setColor(Color.BLUE);
            imageView.setImageBitmap(bitmap);

            imageView.setOnTouchListener(this);
        }


    }
    float x1, x2, y1, y2, dx, dy;
    String direction="";
    String pdirection="";
    @Override
    public boolean onTouch(View v,MotionEvent event) {
        switch(event.getAction()) {
            case (MotionEvent.ACTION_DOWN):
                x1 = event.getX();
                y1 = event.getY();
                break;

            case (MotionEvent.ACTION_UP): {
                x2 = event.getX();
                y2 = event.getY();
                dx = x2 - x1;
                dy = y2 - y1;
                if(dx>100 || dx<-100||dy>100||dy<-100) {


                    // Use dx and dy to determine the direction of the move
                    if (Math.abs(dx) > Math.abs(dy)) {
                        if (dx > 0)
                            direction = direction+"right";
                        else
                            direction = direction+"left";
                    } else {
                        if (dy > 0)
                            direction =direction+ "down";
                        else
                            direction =direction+ "up";
                    }
                }

                if(!pdirection.equalsIgnoreCase(direction))
                {
                    pdirection=direction;
                    pattern=pdirection;
                    Toast.makeText(this,"pdirect="+pdirection,Toast.LENGTH_SHORT).show();
                }
//                canvas.drawLine(x1,y1,x2,y2,paint);
//                imageView.invalidate();

            }

        }
//        Toast.makeText(this,"direction"+direction,Toast.LENGTH_SHORT).show();
        return true;
    }














    @Override
    public void onClick(View v) {
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String pp=sh.getString("pattern","");
        if (pattern.equalsIgnoreCase(pp)){
            Intent i=new Intent(getApplicationContext(),app_login.class);
            startActivity(i);

        }
        else {
            Toast.makeText(this,"Incorrect pattern",Toast.LENGTH_SHORT).show();
        }



    }
}
