
  @app.route('/books', methods=['POST'])
  def create_book():
    body = request.get_json()
    new_title = body.get('title', None)
    new_author = body.get('author', None)
    new_rating = body.get('rating', None)
    search = body.get('search', None)

    try: 
    
      if search:
        selection = Book.query.order_by(Book.id).filter(Book.title.ilike('%{}%'.format(search)))
        current_books = paginate_books(request, selection)

        return jsonify({
          'success': True,
          'books': current_books,
          'total_books': len(selection.all())
        })

      else:
         book = Book(title=new_title, author=new_author, rating=new_rating)
         book.insert()

         selection = Book.query.order_by(Book.id).all()
         current_books = paginate_books(requeset, selection)

         return jsonify({
           'success': True,
           'created': book.id,
           'books': current_books,
           'total_books': len(Book.query.all())
         })

      except: 
        abort(422)


