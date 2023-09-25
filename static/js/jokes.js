window.addEventListener('load', () => {
    if (document.querySelector('#like-button')) {
        const likeButton = document.querySelector('#like-button');
        const dislikeButton = document.querySelector('#dislike-button');
        likeButton.addEventListener('click', () => { register(1); })
        dislikeButton.addEventListener('click', () => { register(-1); })
    }
})

function register(vote) {
    const csrfInput = document.querySelector("input[name='csrfmiddlewaretoken']");
    const csrfToken = csrfInput.value;
    const likes = Number(document.querySelector('#likes').innerHTML);
    const dislikes = Number(document.querySelector('#dislikes').innerHTML);
    const data = {
        'vote': vote,
        'likes': likes,
        'dislikes': dislikes,
    }
    fetch(ajaxURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        const numVotes = data.dislikes + data.likes;
        let voteText = '${numVotes} votes';
        if (numVotes !== 1) voteText += 's';
        document.querySelector('#output').innerHTML = data.msg;
        document.querySelector('#likes').innerHTML = data.likes;
        document.querySelector('#dislikes').innerHTML = data.dislikes;
        document.querySelector('#vote-count').innerHTML = voteText;
    });
}