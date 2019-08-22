const APP_ID = 'c067a0de';
const APP_KEY = 'd35c2a80a1a6f465ea0f1c310dc0ca80	';
const itemsSearch = 'pasta';
const appRequest = `
 https://api.edamam.com/search?q=pasta&app_id=${APP_ID}&app_key=${APP_KEY}`;
// fetch(appRequest)
//   .then(function(response) {
//     console.log(response.json());
//   })
//   .then(function(myJson) {
//     console.log(JSON.stringify(myJson));
//   });

const getRecipes = async () => {
  const response = await fetch(appRequest);
  const data = await response.json();
  displayData(data.hits)
};

getRecipes();

  //function used to display the reciepes to the front end
function displayData(datas){
  //the div that will contain all the info
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
