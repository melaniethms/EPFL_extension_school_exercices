// /index page :


function SaveUserName(){
    if(localStorage != null) {
        UserName = window.prompt("Quel est votre prénom ? ");
        var NameElement = document.getElementById("UserName");
        NameElement.innerText = "Welcome back " + UserName;
        localStorage.setItem ("User Name", UserName);
        alert("welcome " + UserName)
    }
    
}

// /add page :
const addButton = document.getElementById("addButton");
const myText = document.getElementById("myNote");
const content = document.getElementById("content");


function addParagraph(){
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText.value;
    newParagraph.className = "newItem";
    content.appendChild(newParagraph);
    const newItemIdx = content.children.length - 1;
    localStorage.setItem("element-"+newItemIdx, myText.value )
}

SaveUserName();

if(addButton){
    addButton.addEventListener("click", addParagraph);
}

