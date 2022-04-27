const addButton = document.getElementById("addButton");
const removeButton = document.getElementById("removeButton");
const clearButton = document.getElementById("ClearButton");
const myText = document.getElementById("myText");
const content = document.getElementById("content");


function addParagraph(){
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText.value;
    newParagraph.className = "newItem";
    
    content.appendChild(newParagraph);
}

// // pour chaque nouveau paragraphe écrit je veux enregistrer dans le storage un key qui correspond à l'index et une value qui est l'innerText à cet index
// function storeParagraph(){
//     for (newParagraph in content){
//         localStorage.setItem(String(content.indexOf(newParagraph), String(newParagraph.innerText)); 
//     }
// }

function removeLastParagraph(){
    const paragraphs = document.getElementsByClassName("newItem");
    if(paragraphs.length > 0){
        content.removeChild(paragraphs[paragraphs.length - 1])
    }

}

function clearParagraph(){
    const paragraphs = document.getElementsByClassName("newItem");
    for (i in paragraphs) {
        if(paragraphs.length > 0){
            paragraphs.removeChild(i)
    }
    
    }
}

localStorage.clear();
addButton.addEventListener("click", addParagraph);
//addButton.addEventListener("click", storeParagraph);
removeButton.addEventListener("click", removeLastParagraph);
clearButton.addEventListener("click", clearParagraph);

// Exercice :
// -les textes devront apparaître dans le block gris en haut de page
// -button Add item = ajouter un nouveau text dans le block + dans le storage 
// -button Remove last item = enlever le dernier text dans le block + dans le storage + pas d'erreur si on supprime du texte alors qu'il n'y en a plus 
// -button Clear all = enlever tous les textes à l'écran et dans le storage +pas d'erreur si on supprime du texte alors qu'il n'y en a plus 
