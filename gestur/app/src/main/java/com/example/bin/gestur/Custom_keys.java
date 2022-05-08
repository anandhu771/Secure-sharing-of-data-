package com.example.bin.gestur;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;



public class Custom_keys extends BaseAdapter {



    String[] discussionid, studentid, message, msgdate, s_name ,email, photo;
    private Context context;

    public Custom_keys(Context appcontext, String[] discussionid)
    {
        this.context=appcontext;
        this.discussionid=discussionid;


    }

    @Override
    public int getCount() {
        return discussionid.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.customabcd,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tvdate=(TextView)gridView.findViewById(R.id.textView);


        tvdate.setText(discussionid[i]);








        return gridView;
    }

}
