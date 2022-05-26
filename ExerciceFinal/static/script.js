// /index page :


function SaveUserName(){
    if(localStorage.getItem('User Name') == null) {
        UserName = window.prompt("Quel est votre prénom ? ");
        localStorage.setItem ("User Name", UserName);
        alert("welcome " + UserName);
    } 
}

function UseUserName(){
    var UserNameStored = localStorage.getItem('User Name');
    const element = document.getElementById('welcome');
    element.innerHTML = "welcome back " + UserNameStored;
}

// /add page :
const addButton = document.getElementById("addButton");
const myText = document.getElementById("myNote");
const content = document.getElementById("content");

// Cette fonction est fausse :
function addParagraph(){
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText.value;
    newParagraph.className = "newItem";
    content.appendChild(newParagraph);
    const newItemIdx = content.children.length - 1;
    localStorage.setItem("element-"+newItemIdx, myText.value )
}
// Je veux une fonction qui ajoute des notes au doocument text

SaveUserName();
// Comment faire que cette fonction ne tourne qu'à l'ouverture de l'app ?
UseUserName();
//ne fonctionne pas

if(addButton){
    addButton.addEventListener("click", addParagraph);
}

