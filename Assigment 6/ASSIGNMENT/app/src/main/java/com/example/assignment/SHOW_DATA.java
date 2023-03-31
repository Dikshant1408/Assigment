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
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class SHOW_DATA extends AppCompatActivity {

    DatabaseReference reference;
    Button readDataBtn;
    EditText etProductID;
    TextView tvProductName, tvProductPrice, tvProductQuantity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_data);

        readDataBtn = findViewById(R.id.readdataBtn);
        etProductID = findViewById(R.id.etproductID);
        tvProductName = findViewById(R.id.tvProductName);
        tvProductPrice = findViewById(R.id.tvProductPrice);
        tvProductQuantity = findViewById(R.id.tvProductQuantity);

        readDataBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String productID = etProductID.getText().toString();
                if (!productID.isEmpty()){
                    readData(productID);
                } else {
                    Toast.makeText(SHOW_DATA.this,"Please Enter Product ID",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    private void readData(String productID) {

        reference = FirebaseDatabase.getInstance().getReference("Users");
        reference.child(productID).get().addOnCompleteListener(new OnCompleteListener<DataSnapshot>() {
            @Override
            public void onComplete(@NonNull Task<DataSnapshot> task) {

                if (task.isSuccessful()){

                    if (task.getResult().exists()){

                        Toast.makeText(SHOW_DATA.this,"Data read Successfully",Toast.LENGTH_SHORT).show();
                        DataSnapshot dataSnapshot = task.getResult();
                        String productName = String.valueOf(dataSnapshot.child("productName").getValue());
                        String productPrice = String.valueOf(dataSnapshot.child("productPrice").getValue());
                        String productQuantity = String.valueOf(dataSnapshot.child("productQuantity").getValue());
                        tvProductName.setText(productName);
                        tvProductPrice.setText(productPrice);
                        tvProductQuantity.setText(productQuantity);

                    } else {

                        Toast.makeText(SHOW_DATA.this,"User Doesn't Exists",Toast.LENGTH_SHORT).show();

                    }

                } else {

                    Toast.makeText(SHOW_DATA.this,"Failed to read Data",Toast.LENGTH_SHORT).show();

                }
            }
        });

    }
}