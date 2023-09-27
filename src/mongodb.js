const mongoose =require("mongoose")
//the name of the database is LoginSignupPage
mongoose.connect("mongodb://localhost:27017/LoginSignupPage")
.then(()=>{
    console.log("mongodb connected")
})
.catch(()=>{
    console.log("failed to connect mongodb")
})

const LogInSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    password:{
        type:String,
        required:true
    }
})

//collection is name used in these js files, whereas Collection1 is name of the table{collection in mongo} used in mongodb compass
const collection =new mongoose.model("Collection1",LogInSchema)
// const data={
//     name:"Mariam Zareen",
//     password:"123"
// }
// collection.insertMany([data]);

module.exports=collection