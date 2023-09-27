//this is my js file for login and signup form that is my project 1
const express=require('express')
const app=express()
const hbs=require('hbs')
const path=require('path')
const collection=require("./mongodb")
const { read } = require('fs')

const pathTemplates=path.join(__dirname,"../templates")
app.use(express.json())
app.use(express.urlencoded({extended:false}))

//this line is to tell that views(default name) is renamed as pathTemplate
app.set("views",pathTemplates)
app.set("view engine","hbs")


app.get('/',(req,res)=>{
    res.render('login')
})

app.get('/signup.hbs',(req,res)=>{
    res.render('signup')
})
app.post('/signup',async(req,res)=>{
   try{
    const {name,password}=req.body
    const findName=await collection.find({name})
    console.log(findName);
    if(findName.length==0){
    const data=new collection({
        name:name,
        password:password
    })
    await data.save();
    console.log("data saved to databases")
    res.render('home')}
    else {
        console.log("data already exits. Please login");
        res.render('login')
    }
}
catch{
     res.json("eror occured")
}
})

app.post('/login',async(req,res)=>{
   try{
    const {name,password}=req.body
    const findName=await collection.find({name})
    console.log(findName);
    if(findName.length==0){
        console.log("you donot have an account please signup ")
        res.render('signup');
    }
    else{
        res.render('home')
    }
   }
   catch{
    res.json("an error occured")
   }
    
})



app.listen(3000,()=>{
    console.log("port connected")
});






//this is a method of just rendering a static html file using app.use(express.static())

// const static_path= path.join(__dirname, "../public");
// app.use(express.static(static_path));
// app.get("/",(req,res)=>{
//     res.send("hello from mishu");
// })
// app.listen(3000,()=>{
//     console.log("server started running")
// })
