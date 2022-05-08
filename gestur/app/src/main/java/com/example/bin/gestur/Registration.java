package com.example.bin.gestur;


import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.gesture.GestureOverlayView;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.Display;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;

public class Registration extends Activity implements  View.OnTouchListener, View.OnClickListener {


    ImageView imageView;
    EditText ed;

    Bitmap bitmap;
    Canvas canvas;
    Paint paint;
    Button saveB;
    String pattern;






    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);


        imageView = (ImageView) findViewById(R.id.ImageView);
        ed=(EditText)findViewById(R.id.textview);
        saveB=(Button) findViewById(R.id.save);

        saveB.setOnClickListener(this);

        Display currentDisplay = getWindowManager().getDefaultDisplay();
        float dw = currentDisplay.getWidth();
        float dh = currentDisplay.getHeight();

        bitmap = Bitmap.createBitmap((int) dw, (int) dh,
                Bitmap.Config.ARGB_8888);
        canvas = new Canvas(bitmap);
        paint = new Paint();
        paint.setColor(Color.BLUE);
//        paint.setStyle(Paint.Style.FILL_AND_STROKE);
        paint.setStrokeWidth(25);
        imageView.setImageBitmap(bitmap);

        imageView.setOnTouchListener(this);



    }



float x1, x2, y1, y2, dx, dy;
    String direction="";
    String pdirection="";
    String viewp="";
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
//                    if (viewp.equalsIgnoreCase(""))
//                    {
//                        viewp=direction;
//                    }else {
//viewp=viewp+"-"+pdirection;
//                    }
                }

                ed.setText(pattern);
                canvas.drawLine(x1,y1,x2,y2,paint);
                imageView.invalidate();

            }

        }
//        Toast.makeText(this,"direction"+direction,Toast.LENGTH_SHORT).show();
        return true;
    }

    @Override
    public void onClick(View v) {
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed=sh.edit();
        ed.putString("pattern",pattern);
        ed.commit();
        Toast.makeText(this,"pattern"+pattern,Toast.LENGTH_SHORT).show();
        Intent i= new Intent(getApplicationContext(),login.class);
        startActivity(i);














        

    }
}
