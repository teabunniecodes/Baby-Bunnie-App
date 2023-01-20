const buttonAction = document.getElementsByClassName("menu-actions")
let currentDT = document.getElementById("date-time")
let className = "colored-button"

// TODO highlight buttons so I know which one is active at a given time

function dataHandler(data) {
    date = data["date"];
    time = data["time"];
    currentDT.textContent = `${date} ${time}`
}

function fetchData(button) {
    fetch("/tummy_time", {
        headers: {
            "Content-type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(button)
    })
    .then((response) => response.json())
    .then((data) => dataHandler(data))
}

function initButtons() {
    for (let x = 0; x < buttonAction.length; x++) {
        buttonAction[x].addEventListener("click", e => {
            if (buttonAction[x].id === "tummy-time") {
                fetchData("tummy_time");
            }
        });
    }
}

initButtons()