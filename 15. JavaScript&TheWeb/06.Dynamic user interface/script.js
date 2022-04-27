const myButton = document.getElementById("myButton");
const myText = document.getElementById("myText");
const content = document.getElementById("content");
const remove1stParaButton = document.getElementById("remove1stParaButton");
const removeLastParaButton = document.getElementById("removeLastParaButton");
const main = document.getElementById("main");

function addParagraph(){
    const newParagraph = document.createElement("p");
    newParagraph.innerText = myText.value;
    newParagraph.className = "beautiful";
    
    content.appendChild(newParagraph);
}

function removeFirstParagraph(){
    const paragraphs = document.getElementsByClassName("beautiful");
    if(paragraphs.length > 0){
        content.removeChild(paragraphs[0]);
    }

}

function removeLastParagraph(){
    const paragraphs = document.getElementsByClassName("beautiful");
    if(paragraphs.length > 0){
        content.removeChild(paragraphs[paragraphs.length - 1])
    }
}

myButton.addEventListener("click", addParagraph);
remove1stParaButton.addEventListener("click", removeFirstParagraph);
removeLastParaButton.addEventListener("click", removeLastParagraph);

