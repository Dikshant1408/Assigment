package com.example.assignment;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.option_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {

        int id = item.getItemId();

        if (id == R.id.menu_add){
            Intent intent = new Intent(MainActivity.this, ADD_DATA.class);
            startActivity(intent);

            return true;
        }
        else if (id == R.id.menu_show) {
            Intent intent = new Intent(MainActivity.this, SHOW_DATA.class);
            startActivity(intent);

            return true;
        }
        else if (id == R.id.menu_update){
            Intent intent = new Intent(MainActivity.this, UPDATE_DATA.class);
            startActivity(intent);

            return true;
        }
        else if (id == R.id.menu_delete) {
            Intent intent = new Intent(MainActivity.this, DELETE_DATA.class);
            startActivity(intent);

            return true;
        }
        return true;
    }
}