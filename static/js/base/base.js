let menu = document.querySelector('#menu_btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active')
}

window.onscroll = () =>{

    if(window.scrollY > 0){
        document.querySelector('.header').classList.add('active');
    }else{
        document.querySelector('.header').classList.remove('active');
    }
    menu.classList.remove('fa-times');
    navbar.classList.remove('active')
}

window.onload = () =>{

    if(window.scrollY > 0){
        document.querySelector('.header').classList.add('active');
    }else{
        document.querySelector('.header').classList.remove('active');
    }
   
}

document.querySelector('.home').onmousemove = (e) =>{
    document.querySelectorAll('.home_parallax').forEach(elm =>{
        let speed = elm.getAttribute('data-speed');

        let x = (window.innerWidth - e.pageX * speed) / 90;
        let y = (window.innerHeight - e.pageY * speed) / 90;

        elm.style.transform = `translateX(${y}px) translateY(${x}px)`;
    });
}



document.querySelector('.home').onmouseleave = () =>{
    document.querySelectorAll('.home_parallax').forEach(elm =>{
        let speed = elm.getAttribute('data-speed');
        elm.style.transform = `translateX(0px) translateY(0px)`;
    });
}