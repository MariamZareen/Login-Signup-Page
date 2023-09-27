// this file is js code for registration form ie my project 2
const express=require("express")
const app=express();
const path=require("path")
const hbs=require('hbs')
const User=require("./models/db2")


const html_path=path.join(__dirname,"../templates2/views")
const partial_path=path.join(__dirname,"../templates2/partials")
app.set("view engine","hbs")
app.set("views",html_path)
hbs.registerPartials(partial_path)

// this is to make postman or thunderclient understand the input data
app.use(express.json())
// this line is to render the input data on the browser
app.use(express.urlencoded({extended:false}))


app.get("/",(req,res)=>{
    res.render("index")
})
app.get("/register",(req,res)=>{
    res.render("hi")
})
app.post("/Register", async(req,res)=>{
    try{
    const password=req.body.password;
    const confirmPassword=req.body.confirmPassword;
    if(password===confirmPassword){
        const email=req.body.email;
        const res=await User.find({email});
        if(res) alert("User already present")
        else {
       const userList = new User({
        name:req.body.name,
        email:req.body.email,
        password:req.body.password,
        confirmPassword:req.body.confirmPassword
       })
       const registered = await userList.save();
       res.render("hi")
      }
    }
    else{
        res.send("Password and confirm password doesnot match");
    }
    }
    catch(err){
        res.send("there was some technical error connecting")
      res.status(404).send()
    }
})

app.listen(4000,()=>{
    console.log("app running on port 4000")
})