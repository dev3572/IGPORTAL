/**
 * Created by lenovo on 9/6/2016.
 */
<!--form validation-->
        function validate(){
            var x=document.forms['signupform']['name'].value;
            if(x==null||x==""){
                alert("Name must be filled");
                return false;
            }
            var y=document.forms['signupforms']['email'].value;
            if(y==null||y==""){
                alert("email must be filled");
                return false;
            }
            var z=document.forms['signupforms']['password'].value;
            var a=document.forms['signupforms']['repassword'].value;
            if(z==null||z.length<6){
                alert("password should be of at least 6 characters ");
                return false;
            }
            if(z!=a){
                alert("passwords do not match");
                return false;
            }
            var b=document.forms['signupforms']['course'].value;
            if(b==null||b==""){
                alert("course cannot be left empty");
                return false;
            }
            var c=document.forms['signupforms']['year'].value;
            if(c==null||c==""){
                alert("year cannot be left empty");
                return false;
            }
            var d=document.forms['signupforms']['branch'].value;
            if(d==null||d==""){
                alert("branch cannot be left empty");
                return false;
            }
            var e=document.forms['signupforms']['roll'].value;
            if(e==null||e==""){
                alert("roll number cannot be left empty");
                return false;
            }
            var f=document.forms['signupforms']['reg'].value;
            if(f==null||f==""){
                alert(" registration number be left empty");
                return false;
            }

        }
