var emp1={firstname:"Anna",lastname:"Frost"}
var emp2={firstname:"Peter",lastname:"Guiller"}

function invite(g1,g2){
    console.log(g1+" "+this.firstname+" "+this.lastname+ " , "+g2)
}

// takes only arguments as any type 

// invite.call(emp1,emp1.firstname,emp1.lastname)
// invite.call(emp2,"Hello","Nice to meet you")

// same like call but takes argumentin array  apply(objName,[itm1,itm2])
// invite.apply(emp1,["Hello","How do you do"])
// invite.apply(emp2,["Hello","How do you do"])

// Bind not immdetialtey invoke the function ,instead its return new function that can call later
// const inv1=invite.bind(emp1)
// const inv2=invite.bind(emp2)
// inv1("Hello","How are you")
// inv2("Hello","Beta")



// // Notes:
// Method	Invokes Function Immediately?	How Arguments Are Passed	Returns
// call	    Yes	                            Comma-separated list	    Function's result
// apply	Yes	                            Array or array-like object	Function's result
// bind	    No	                            preset, then rest           New function


// /lexical enivroment 
// scope is global 
// var name="Abhishek"
// function getName(){
//     console.log(name)
// }

// getName()

// local scope
// function getName(){
//     let name="abhishek"
//     console.log(name)
// }
// getName()
// console.log(name)

// Nested scope 
// function getName(){
//     let lastName="Manglam"
//     function getLastName(){
//         console.log(lastName)
//     }
//     getLastName()
// }

// getName()

// function outer() {
//     let outerVar = "I'm in the outer scope!";

//     return function inner() {
//         console.log(outerVar);
//     }
// }

// const closure = outer();

// closure();
// closure();

function x(){
    // var i=1
    for (let i =0;i<5;i++){
    setTimeout(()=>{
            console.log(i)
        },3000)
    }
    console.log("I am waiting to run ")
}
x()