// Navigation function
function showPage(page) {

    document.getElementById("homePage").style.display = "none";
    document.getElementById("predictionPage").style.display = "none";

    if (page === "home") {
        document.getElementById("homePage").style.display = "block";
    } else {
        document.getElementById("predictionPage").style.display = "block";
    }
}

// Prediction function
function predict() {

    let date = document.getElementById("date").value;
    let time = document.getElementById("time").value;

    fetch("http://127.0.0.1:5000/predict")
        .then(res => res.json())
        .then(data => {

            let val = data[0].Predicted_Hospitalized;

            let level;
            if (val < 2000) level = 1;
            else if (val < 4000) level = 2;
            else if (val < 6000) level = 3;
            else if (val < 8000) level = 4;
            else level = 5;

            document.getElementById("result").innerHTML = `
                Date: ${date} <br>
                Time: ${time} <br>
                Estimated People Affected - Tamil Nadu: ${level}
            `;
        });
}