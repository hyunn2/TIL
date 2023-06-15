<script>
  // let message;

  // fetch("http://127.0.0.1:8000/").then((response) => {
  //   response.json().then((json) => {
  //     message = json.msg;
  //   });
  // });

  let question_list = []

  function get_question_list() {
    fetch("http://localhost:8000/api/question/list").then((res) => {
      res.json().then((json) => {
        question_list = json
      })
    })
  }

  get_question_list()
</script>

<!-- <h1>{message}</h1> -->

<ul>
  {#each question_list as question}
    <li>
      {question.subject}
    </li>
  {/each}
</ul>