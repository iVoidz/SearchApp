const APP_ID = 'c067a0de';
const APP_KEY = 'd35c2a80a1a6f465ea0f1c310dc0ca80	';
const itemsSearch = 'pasta';
const input = document.querySelector('#search');
let userInput;
input.addEventListener("keydown", e => {
  const keyName = event.key || event.which;
  if(keyName === "Enter"){
    getRecipes(input.value)
    input.value = ''
  }
});


const getRecipes = async (userSearch) => {
  const appRequest = `
   https://api.edamam.com/search?q=${userSearch}&app_id=${APP_ID}&app_key=${APP_KEY}`
  const response = await fetch(appRequest);
  const data = await response.json();
  displayData(data.hits)
};

getRecipes();

function displayData(datas){
  const contentDiv = document.querySelector("#main");
  contentDiv.innerHTML = '';
  datas.map( data => {
  contentDiv.innerHTML += `<a class="link" href=${data.recipe.url} target="_blank">
    <div class="contain">
      <h1 class="title">${data.recipe.label}</h1>
      <img class="picture" src=${data.recipe.image}>
    </div>
  </a>`;
  });
};
