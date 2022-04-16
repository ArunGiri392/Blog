console.log("arun");
alert("Hello! I am an alert box!!");




const value = document.querySelectorAll(".stars a");
value.forEach((star,index) => {
    
    star.addEventListener("click",()=>{
        // numberofuserreviews++;

        
        console.log(index+1);
        // newRating = (index + 1) / numberofuserreviews
        // console.log(newRating);
        // console.log(index+1);
    })
   
});
