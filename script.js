
function getRandomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}


const changeColorBtn = document.getElementById('change-color-btn');


changeColorBtn.addEventListener('click', () => {

    const currentColor = document.body.style.backgroundColor;


    const newColor = getRandomColor();


    document.body.style.backgroundColor = newColor;
});