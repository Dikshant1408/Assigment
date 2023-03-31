package com.example.assignment;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;

public class UPDATE_DATA extends AppCompatActivity {

    DatabaseReference reference;
    private Button updateBtn;
    private TextView prodID, prodName, prodPrice, prodQuantity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_update_data);

        updateBtn = findViewById(R.id.updateBtn);
        prodID = findViewById(R.id.productID);
        prodName = findViewById(R.id.productName);
        prodPrice = findViewById(R.id.productPrice);
        prodQuantity = findViewById(R.id.productQuantity);

        updateBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String productID = prodID.getText().toString();
                String productName = prodName.getText().toString();
                String productPrice = prodName.getText().toString();
                String productQuantity = prodQuantity.getText().toString();
                
                updateData(productID, productName, productPrice, productQuantity);

            }
        });

    }

    private void updateData(String productID, String productName, String productPrice, String productQuantity) {

        HashMap User = new HashMap();
        User.put("productName",productName);
        User.put("productPrice",productPrice);
        User.put("productQuantity",productQuantity);
        reference = FirebaseDatabase.getInstance().getReference("Product Info");
        reference.child(productID).updateChildren(User).addOnCompleteListener(new OnCompleteListener() {
            @Override
            public void onComplete(@NonNull Task task) {

                if (task.isSuccessful()){

                    prodID.setText("");
                    prodName.setText("");
                    prodPrice.setText("");
                    prodQuantity.setText("");
                    Toast.makeText(UPDATE_DATA.this,"Data Updated Successfully",Toast.LENGTH_SHORT).show();

                }else {

                    Toast.makeText(UPDATE_DATA.this,"Failed to Update Data",Toast.LENGTH_SHORT).show();

                }

            }
        });

    }
}