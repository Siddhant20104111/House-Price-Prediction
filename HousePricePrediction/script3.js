const forms= document.querySelector(".forms"),
      pwShowHide = document.querySelectorAll(".eye-icon"),
      links = document.querySelectorAll(".link");


/*function myFunction(){
    var x =document.getElementsByClassName("input");
    if (x.type === "password"){
        x.text= "text";
       }
    else{
        x.type="password";
    }
}*/

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
        
        pwFields.forEach(password => {
            if(password.type === "password"){
                password.type = "text";
                eyeIcon.classList.replace("bx-hide","bx-show");
                return;
            }
            password.type = "password";
            eyeIcon.classList.replace("bx-show","bx-hide");
        })
    })
} )
function register(){
    var emal=document.forms.reg.emal.value;
    var pwd=document.forms.reg.pwd.value;

    var regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?w+)*(\.\w{2,3})+$/g;
    var regpassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;

    if (emal=="" && pwd==""){
      window.alert("Please enter all the fields");
      document.reg.dob.focus();
      return false;
    }

    if (emal=="" ){
        window.alert("Please enter your Email Address");
        document.reg.emal.focus();
        return false;
    }


    if( !regEmail.test(emal)){
        window.alert("Please Enter valid Email Address Example: siddhantdarekar1010@gmail.com ");
        document.reg.emal.focus();
        return false;
    }

    if(pwd==""){
        window.alert("Please Enter Password");
        document.reg.pwd.focus();
        return false;
    }
    if(pwd.length<=7 || pwd.length>=15 || !regpassword.test(pwd)){
        window.alert("Please Enter having 7 and 15 cahracters which contains atleast one special character and atleast one digit ");
        document.reg.pwd.focus();
        return false;
    }
}

