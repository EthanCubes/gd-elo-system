const search = document.getElementById("search");
const lucky = document.getElementById("lucky");
const query = document.getElementById("query");

let playerList;

search.addEventListener("click", function() {searchPlayer(query.value)});
lucky.addEventListener("click", function() {getUsers()}); // to make sure that users are loaded before they're processed

async function searchPlayer(query) {
    const url = "http://localhost:5000/api/search?name=" + query;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    return(data);
}

function luckySearch() {
    playerList = playerList.split("\n");
    let username = playerList[Math.floor(Math.random()*playerList.length)];
    searchPlayer(username);
}

function getUsers() {
    const url = "assets/players.txt"
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text()
        })
        .then(data => {
            playerList = data;
            luckySearch();
        })
        .catch(error => {
            console.error("Error", error.message);
        });
}