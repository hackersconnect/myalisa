//copy menu for media display

function copyMenu() {
    //copy from one class to another

    var mainNav=document.querySelector('.header-nav nav');
    var navPlace=document.querySelector('.off-canvas nav');

    navPlace.innerHTML=mainNav.innerHTML;

    
}
copyMenu();

//toggle sidemenu

const menuButton=document.querySelector('.trigger'),
      closeButton=document.querySelector('.t-close'),
      addMenu=document.querySelector('.site');

menuButton.addEventListener('click', function() {
    addMenu.classList.toggle('showmenu')
})

closeButton.addEventListener('click', function() {
    addMenu.classList.remove('showmenu')
});




//show Passwords on forms

const paswd = document.getElementById("password");
const checkButton = document.getElementById("check")

checkButton.addEventListener('click', function(){
    if(checkButton.checked){
        paswd.type="text"
    }
    else{
        paswd.type="password"
    }
})


const myPass = document.getElementById("mypassword");
const checkBtn = document.getElementById("mycheck")
checkBtn.addEventListener('click', function(){
    if(checkBtn.checked){
        myPass.type="text"
    }
    else{
        myPass.type="password"
    }
})


let password = document.getElementById("mypassword2");
let checkbox = document.getElementById("mycheck");

checkbox.onclick = function(){
    if (checkbox.checked) {
        password.type = "text";
    }else{
        password.type = "password";
    }
}
