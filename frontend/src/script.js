const search = document.getElementById("search");
const lucky = document.getElementById("lucky");
const query = document.getElementById("query");

let playerList;
let playerData;

const loading = document.getElementById("loading");
const info = document.getElementById("info");

search.addEventListener("click", function() {searchPlayer(query.value)});
lucky.addEventListener("click", function() {getUsers()}); // to make sure that users are loaded before they're processed

async function searchPlayer(query) {
    loading.innerHTML = "<h1>Loading...</h1>"
    loading.style.display = "block";
    info.style.display = "none";
    const url = "http://localhost:5000/api/search?name=" + query;
    try {
        const response = await fetch(url);
    }
    catch {
        alert("Connection error.")
        loading.innerHTML = "<h1>Load Failed: Connection error</p><button onclick=\"reloadPage()\">Refresh Page</button>"
    }
    const data = await response.json();
    playerData = data;
    loading.style.display = "none";
    updateStats();
}

function luckySearch() {
    playerList = playerList.split("\n");
    let username = playerList[Math.floor(Math.random()*playerList.length)];
    searchPlayer(username);
}

function getUsers() {
    const url = "assets/players.txt";
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

function updateStats() {
    const name = document.getElementById("name");
    const elo = document.getElementById("elo");
    const stars = document.getElementById("stars");
    const moons = document.getElementById("moons");
    const secretCoins = document.getElementById("secretCoins");
    const userCoins = document.getElementById("userCoins");
    const easyDemons = document.getElementById("easyDemons");
    const mediumDemons = document.getElementById("mediumDemons");
    const hardDemons = document.getElementById("hardDemons");
    const insaneDemons = document.getElementById("insaneDemons");
    const extremeDemons = document.getElementById("extremeDemons");
    info.style.display = "block";

    name.innerHTML = playerData[0].name;
    elo.innerHTML = playerData[1];
    stars.innerHTML = "Stars: " + playerData[0].stars;
    moons.innerHTML = "Moons: " + playerData[0].moons;
    secretCoins.innerHTML = "Secret Coins: " + playerData[0].secretCoins;
    userCoins.innerHTML = "User Coins: " + playerData[0].userCoins;
    easyDemons.innerHTML = "Easy Demons: " + playerData[0].easyDemons;
    mediumDemons.innerHTML = "Medium Demons: " + playerData[0].mediumDemons;
    hardDemons.innerHTML = "Hard Demons: " + playerData[0].hardDemons;
    insaneDemons.innerHTML = "Insane Demons: " + playerData[0].insaneDemons;
    extremeDemons.innerHTML = "Extreme Demons: " + playerData[0].extremeDemons;
}

function reloadPage() {
    window.location.reload();
}