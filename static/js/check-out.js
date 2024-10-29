//copy menu for media display

function copyMenu() {
    //copy from one class to another

    var topNav=document.querySelector('.header-top .wrapper');
    var topPlace=document.querySelector('.off-canvas .thetop-nav');

    topPlace.innerHTML=topNav.innerHTML;
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

const dropmenu=document.querySelectorAll('.has-child .icon-small');
dropmenu.forEach((menu) => menu.addEventListener('click', toggle));

function toggle(e) {
    e.preventDefault();
    dropmenu.forEach((item) => item != this ? item.closest('.has-child').classList.remove('expand') : null);
    if(this.closest('.has-child').classList != 'expand');
    this.closest('.has-child').classList.toggle('expand')
};
