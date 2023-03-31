package com.example.assignment;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.assignment.databinding.ActivityMainBinding;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.ktx.Firebase;

public class ADD_DATA extends AppCompatActivity {

    private String productID, productName, productPrice, productQuantity;
    FirebaseDatabase db;
    DatabaseReference reference;
    private Button addData;
    private TextView prodID, prodName, prodPrice, prodQuantity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_data);

        addData = findViewById(R.id.addDataBtn);
        prodID = findViewById(R.id.productID);
        prodName = findViewById(R.id.productName);
        prodPrice = findViewById(R.id.productPrice);
        prodQuantity = findViewById(R.id.productQuantity);

        addData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                productID = prodID.getText().toString();
                productName = prodName.getText().toString();
                productPrice = prodPrice.getText().toString();
                productQuantity = prodQuantity.getText().toString();

                if (!productID.isEmpty() && !productName.isEmpty() && !productPrice.isEmpty() && !productQuantity.isEmpty()){
                    Users users = new Users(productID, productName, productPrice, productQuantity);
                    db = FirebaseDatabase.getInstance();
                    reference = db.getReference("Product Info");
                    reference.child(productID).setValue(users).addOnCompleteListener(new OnCompleteListener<Void>() {
                        @Override
                        public void onComplete(@NonNull Task<Void> task) {

                            prodID.setText("");
                            prodName.setText("");
                            prodPrice.setText("");
                            prodQuantity.setText("");
                            Toast.makeText(ADD_DATA.this,"Data Successfully  Added",Toast.LENGTH_SHORT).show();

                        }
                    });
                }

            }
        });
    }
}