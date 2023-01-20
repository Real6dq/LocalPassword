package club.iml1.localpassword2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText lengthEditText;
    private EditText nameEditText;
    private EditText passwordEditText;
    private EditText birthdateEditText;
    private EditText websiteEditText;
    private TextView passwordTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        lengthEditText = findViewById(R.id.length_edit_text);
        nameEditText = findViewById(R.id.name_edit_text);
        passwordEditText = findViewById(R.id.password_edit_text);
        birthdateEditText = findViewById(R.id.birthdate_edit_text);
        websiteEditText = findViewById(R.id.website_edit_text);
        passwordTextView = findViewById(R.id.password_text_view);

        Button generateButton = findViewById(R.id.generate_button);
        generateButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int length = Integer.parseInt(lengthEditText.getText().toString());
                String name = nameEditText.getText().toString().toLowerCase();
                String password = passwordEditText.getText().toString().toLowerCase();
                String birthdate = birthdateEditText.getText().toString().toLowerCase();
                String website = websiteEditText.getText().toString().toLowerCase();
                String generatedPassword = PasswordGenerator.generate(length, name, password, birthdate, website);
                passwordTextView.setText(generatedPassword);
            }
        });
    }
}