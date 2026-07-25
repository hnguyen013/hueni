/**
 * Quiz demo (Task 3.5) — flashcard tương tác, thuần client-side.
 * Không gửi request server, không lưu kết quả.
 *
 * Cấu trúc DOM mong đợi (xem templates/showcase/_quiz.html):
 *   .quiz-card
 *     .quiz-progress          (span hiển thị "Câu x/y")
 *     .quiz-progress-bar      (thanh tiến trình)
 *     .quiz-questions
 *       .quiz-question[data-index]
 *         .quiz-choice[data-correct="true|false"]
 *         .quiz-explanation
 *         .quiz-next
 *     .quiz-done
 *       .quiz-restart
 */
(function () {
  'use strict';

  var CORRECT_CLASSES = ['bg-secondary-container', 'text-on-secondary-container', 'border-secondary'];
  var WRONG_CLASSES = ['bg-error-container', 'text-on-error-container', 'border-error'];

  function initQuizCard(card) {
    var questions = Array.prototype.slice.call(card.querySelectorAll('.quiz-question'));
    var progressLabel = card.querySelector('.quiz-progress');
    var progressBar = card.querySelector('.quiz-progress-bar');
    var doneEl = card.querySelector('.quiz-done');
    var restartBtn = card.querySelector('.quiz-restart');
    var total = questions.length;

    if (!total) return;

    function updateProgress(index) {
      if (progressLabel) {
        progressLabel.textContent = 'Câu ' + (index + 1) + '/' + total;
      }
      if (progressBar) {
        progressBar.style.width = Math.round(((index + 1) / total) * 100) + '%';
      }
    }

    function showQuestion(index) {
      questions.forEach(function (q, i) {
        q.classList.toggle('hidden', i !== index);
      });
      if (doneEl) doneEl.classList.add('hidden');
      updateProgress(index);
    }

    function resetQuestion(questionEl) {
      var choices = questionEl.querySelectorAll('.quiz-choice');
      choices.forEach(function (choice) {
        choice.disabled = false;
        choice.classList.remove.apply(choice.classList, CORRECT_CLASSES);
        choice.classList.remove.apply(choice.classList, WRONG_CLASSES);
        choice.classList.add('border-outline-variant');
      });
      var explanation = questionEl.querySelector('.quiz-explanation');
      if (explanation) explanation.classList.add('hidden');
      var nextBtn = questionEl.querySelector('.quiz-next');
      if (nextBtn) nextBtn.classList.add('hidden');
      questionEl.dataset.answered = 'false';
    }

    questions.forEach(function (questionEl) {
      var choices = questionEl.querySelectorAll('.quiz-choice');
      var explanation = questionEl.querySelector('.quiz-explanation');
      var nextBtn = questionEl.querySelector('.quiz-next');

      choices.forEach(function (choice) {
        choice.addEventListener('click', function () {
          if (questionEl.dataset.answered === 'true') return;
          questionEl.dataset.answered = 'true';

          choices.forEach(function (c) {
            c.disabled = true;
            var isCorrect = c.dataset.correct === 'true';
            c.classList.remove('border-outline-variant');
            c.classList.add.apply(c.classList, isCorrect ? CORRECT_CLASSES : []);
            if (!isCorrect && c === choice) {
              c.classList.add.apply(c.classList, WRONG_CLASSES);
            } else if (!isCorrect) {
              c.classList.add('opacity-60');
            }
          });

          if (explanation) explanation.classList.remove('hidden');
          if (nextBtn) nextBtn.classList.remove('hidden');
        });
      });

      if (nextBtn) {
        nextBtn.addEventListener('click', function () {
          var currentIndex = questions.indexOf(questionEl);
          if (currentIndex < total - 1) {
            showQuestion(currentIndex + 1);
          } else {
            questions.forEach(function (q) { q.classList.add('hidden'); });
            if (doneEl) doneEl.classList.remove('hidden');
          }
        });
      }
    });

    if (restartBtn) {
      restartBtn.addEventListener('click', function () {
        questions.forEach(resetQuestion);
        showQuestion(0);
      });
    }

    showQuestion(0);
  }

  function init() {
    var cards = document.querySelectorAll('.quiz-card');
    cards.forEach(initQuizCard);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
