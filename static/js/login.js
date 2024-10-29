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




//show dropmenus

