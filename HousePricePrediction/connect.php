<?php
    $servername = "localhost";
    $username = "root";
    $passwd = "";
    $database_name = "mlconnectivity";

    $conn = new mysqli($servername,$username,$passwd,$database_name);
if(isset($_POST['kalpesh'])){
    $full_name = $_POST['fullname'];
    $dateofbirth = $_POST['dob'];
    $email = $_POST['emal'];
    $mobilenumber = $_POST['mobno'];
    $password = $_POST['pwd'];
   
    

    if(mysqli_connect_error()){
        die('Connect Error('. mysqli_connect_errno().')'.mysqli_connect_error());
    }else{
        $SELECT = "SELECT Email_ID From mlconnection Where Email_ID = ? Limit 1";
        $INSERT = "INSERT Into mlconnection (FullName,Birth_Date,Email_ID,mobile_no,password)
        values(?,?,?,?,?)";

        $stmt = $conn->prepare($SELECT);
        $stmt->bind_param("s",$email);
        $stmt->execute();
        $stmt->bind_result($email);
        $stmt->store_result();
        $rnum = $stmt->num_rows;

        if ($rnum==0){
            $stmt->close();
            $stmt = $conn->prepare($INSERT);
            $stmt->bind_param("sssis",$full_name,$dateofbirth,$email,$mobilenumber,$password);
            $stmt->execute();
            echo "New record inserted successfully";
        }
        else{
            echo "Someone already register using this email";
        }
        $stmt->close();
        $conn->close();
    }
}
   


?>