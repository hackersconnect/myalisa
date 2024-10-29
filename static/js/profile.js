var sidebarOpen=false;

var sidebar=document.getElementById("nav-list")

function openSideBar() {    
    if(!sidebarOpen){
        sidebar.classList.add('sidebar-responsive')
        sidebarOpen=true;
    }
}

function closeSidebar() {
    if(sidebarOpen) {
        sidebar.classList.remove('sidebar-responsive')
        sidebarOpen=false;
    }
}