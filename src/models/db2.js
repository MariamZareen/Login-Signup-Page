const mongoose=require("mongoose")

mongoose.connect("mongodb://localhost:27017/RegistrationForm")
.then(()=>{
    console.log("database for registration form connected");
})
.catch((err)=>{
    console.log("cannot connect registration database")
})

const registrationSchema = new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true
    },
    password:{
        type:String,
        required:true
    },
    confirmPassword:{
        type:String,
        required:true,
    }
})

const User =new mongoose.model("User",registrationSchema);

module.exports=User;