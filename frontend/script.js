document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('platformSelection').addEventListener('change', function() {
        const inputField = document.getElementById('usernameInput');

        switch (this.value) {
            case 'youtube': 
                inputField.placeholder = "@Youtuber";
                break;

            case 'instagram':
                inputField.placeholder = "@InstagramUser";
                break;
        }
    });
    
    document.getElementById('redirectToAnalytics').addEventListener('click', function() {
        const platformSelection = document.getElementById('').value;
        console.log("hi");
        const userInput = document.getElementById('usernameInput').value;

        if (!userInput) {
            alert('Please enter a username!');
            return;
        }

        let redirectURL= "";
        switch (platformSelection) {
            case 'youtube':
                // This is the analytics page for YouTube
                redirectURL = "analytics.html";
                break;

            case 'instagram':
                // This is the analytics page for Instagram
                redirectURL = "instagram_analytics.html";
                break;
        }

        window.location.href = redirectURL;
    });

});
