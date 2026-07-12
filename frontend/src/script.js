const search = document.getElementById("search");
const lucky = document.getElementById("lucky");
const query = document.getElementById("query");

let playerList;

search.addEventListener("click", function() {searchPlayer(query.value)});
lucky.addEventListener("click", function() {getUsers()}); // to make sure that users are loaded before they're processed

function searchPlayer(query) {
    console.log(query)
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