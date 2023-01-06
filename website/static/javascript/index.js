const buttonAction = document.getElementsByClassName("menu-actions")

function fetchData(button) {
    fetch("/tummy_time", {
        headers: {
            "Content-type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(button)
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}

function checkButton() {
    for (let x = 0; x < buttonAction.length; x++) {
        buttonAction[x].addEventListener("click", e => {
            if (buttonAction[x].id === "tummy-time") {
                fetchData(buttonAction[x].value);
            }
        });
    }
}

checkButton()