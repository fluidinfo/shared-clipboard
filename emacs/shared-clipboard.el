;; You'll need fluiddb.el, available from
;; https://github.com/hdurer/fluiddb.el

(require 'fluiddb)

(setq *fluiddb-credentials* '("USERNAME" . "PASSWORD"))

(defun insert-clipboard (who)
  "Fetch the contents of the given user's clipboard tag from Fluidinfo and
   insert them into the buffer. If there are no objects with the tag, display
   a message to indicate that the clipboard is empty.

   TODO: handle 404 if tag doesn't exist in the 'has' query, other errors."
  (interactive "sInsert the clipboard of which user? ")
  (let*
      ((user (if (equal who "") (car *fluiddb-credentials*) who))
       (tag (format "%s/clipboard" user))
       (result (fluiddb-query-objects-tag-values (format "has %s" tag) (list tag)))
       (object (cdr (car (cdr (car (car (cdr result))))))))
    (if object
        (insert (cdr (car (cdr (car (cdr (car object)))))))
      (message "Remote clipboard is empty."))))

(defun clear-clipboard (who)
  "Remove the tag holding the given user's clipboard from Fluidinfo."
  (interactive "sClear the clipboard of which user? ")
  (let
      ((tag (format "%s/clipboard" (if (equal who "") (car *fluiddb-credentials*) who))))
    (fluiddb-delete-objects-tag-values (format "has %s" tag) (list tag))))

(defun set-clipboard (who)
  "Set the tag holding the given user's clipboard in Fluidinfo to
   the contents of the current buffer selection.

   TODO: handle region not set, errors."
  (interactive "sSet the region as the clipboard of which user? ")
  (let*
      ((user (if (equal who "") (car *fluiddb-credentials*) who))
       (tag (format "%s/clipboard" user)))
    (clear-clipboard user)
    (fluiddb-set-object-about-tag-value user tag (buffer-substring (region-beginning) (region-end)))))
