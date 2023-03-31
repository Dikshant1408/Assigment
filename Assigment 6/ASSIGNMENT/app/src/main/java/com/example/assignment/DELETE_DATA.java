package com.example.assignment;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DELETE_DATA extends AppCompatActivity {

    private Button DeleteBtn;
    private EditText etproductID;
    DatabaseReference reference;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_delete_data);

        DeleteBtn = findViewById(R.id.deletedataBtn);
        etproductID = findViewById(R.id.etproductID);

        DeleteBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String productID = etproductID.getText().toString();
                if (!productID.isEmpty()){

                    deleteData(productID);

                }else{

                    Toast.makeText(DELETE_DATA.this,"Please Enter Username",Toast.LENGTH_SHORT).show();
                }
                
            }
        });

    }

    private void deleteData(String productID) {

        reference = FirebaseDatabase.getInstance().getReference("Users");
        reference.child(productID).removeValue().addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {

                if (task.isSuccessful()){

                    Toast.makeText(DELETE_DATA.this,"Data Deleted Successfully",Toast.LENGTH_SHORT).show();
                    etproductID.setText("");


                }else {

                    Toast.makeText(DELETE_DATA.this,"Data Failed to Delete",Toast.LENGTH_SHORT).show();


                }

            }
        });

    }
}