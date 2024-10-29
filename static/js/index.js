//copy menu for media display

function copyMenu() {
    //copy from one class to another

    var mainNav=document.querySelector('.header-nav nav');
    var navPlace=document.querySelector('.off-canvas nav');

    navPlace.innerHTML=mainNav.innerHTML;

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

const swiper= new Swiper('.swiper', {
    loop:true,
    

    //pagination

    pagination: {
        el: '.swiper-pagination',
    },
});

//show search

const searchButton = document.querySelector('.t-search');
      tClose = document.querySelector('.search-close');
      showClass = document.querySelector('.site');

searchButton.addEventListener('click', function() {
    showClass.classList.toggle('showsearch')
})
tClose.addEventListener('click', function() {
    showClass.classList.remove('showsearch')
});


