let navbar=document.querySelector('.navbar');
navbar.addEventListener('click',()=>{
    let menu=document.querySelector('.menu');
    
    if(menu.style.display=='none')
       menu.style.display='block';
    
});
console.log(5);
console.log("Hi");

function setLanguage(language) {
    if (language === 'en') {
        // Set English text visible and Marathi text hidden
        document.querySelectorAll('[id$="-en"]').forEach(element => element.style.display = 'inline');
        document.querySelectorAll('[id$="-mr"]').forEach(element => element.style.display = 'none');
    } else if (language === 'mr') {
        // Set Marathi text visible and English text hidden
        document.querySelectorAll('[id$="-en"]').forEach(element => element.style.display = 'none');
        document.querySelectorAll('[id$="-mr"]').forEach(element => element.style.display = 'inline');
    }
}