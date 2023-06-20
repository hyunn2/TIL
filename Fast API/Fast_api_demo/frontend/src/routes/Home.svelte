<script>
  import fastapi from "../lib/api"
  import { link } from 'svelte-spa-router'

  let question_list = []

  function get_question_list() {
    fastapi('get', '/api/question/list', {}, (json) => {
      question_list = json
    })
  }
  get_question_list()

</script>

<div class="container my-3">
  <!-- 글 리스트 -->
  <table class="table">
    <thead>
      <tr class="table-Success">
        <th>번호</th>
        <th>제목</th>
        <th>작성일시</th>
      </tr>
    </thead>
    <tbody>
      {#each question_list as question, i}
      <tr>
        <td>{i + 1}</td>
        <td>
          <a use:link href="/detail/{question.id}">{question.subject}</a>
        </td>
        <td>
          {question.create_date}
        </td>
      </tr>
      {/each}
    </tbody>
  </table>
  <a use:link href="/question-create" class="btn btn-primary">질문 등록</a>

  <br>
  <br>

  <!-- 채팅 -->
  <body>
    <div class="container">
      <h2 class="my-3">Websocket Chat</h2>
      <h3>Your ID: <span id="ws-id"></span></h3>
      <form action="" onsubmit="sendMessage(event)">
        <div class="input-group mb-3">
          <input type="text" id="messageText" autocomplete="off" placeholder="Message">
          <button class="btn btn-primary" type="submit" id="button-addon2">Send</button>
        </div>
      </form>
      <ul id="messages"></ul>
    </div>
    <script>
      let client_id = Date.now() % 10000
      document.querySelector("#ws-id").textContent = client_id;
      let ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
      ws.onmessage = function(event) {
          let messages = document.getElementById('messages')
          let message = document.createElement('li')
          let content = document.createTextNode(event.data)
          message.appendChild(content)
          messages.appendChild(message)
      }
      function sendMessage(event) {
          let input = document.getElementById("messageText")
          ws.send(input.value)
          input.value = ''
          event.preventDefault()
      }
    </script>
  </body>
</div>