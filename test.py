 class EventModelTests(TestCase):
    c = Client()

    @classmethod
    def setUpTestData(cls):


        # dec vars
        today = timezone.now()
        tomorrow = timezone.now() + timedelta(days=1)
        start_date = today.date()
        start_time = today.time()
        end_date = tomorrow.date()
        end_time = start_time

        # create auth user
        User.objects.create(
            username='TestUser',
            email='test@user.com',
            password='password'
        )

        # create attendees for event
        for i in range(5):
            username = 'TestUser%s' % i
            email = 'test%s@user.com' % i
            User.objects.create(
                username=username,
                email=email,
                password='password'
            )

        # Create Events
        for i in range(5):
            event_name = 'Test Event %s' % i
            Event.objects.create(
                name=event_name,
                event_type='Combat',
                creator=User.objects.get(pk=1),
                start_date=start_date,
                start_time=start_time,
                end_date=end_date,
                end_time=end_time,
                location='Sol',
                date_created=timezone.now(),
                description=lorem.paragraph()
            )

    def test_event_associated_to_auth_user(self):
        # check if event will return creator
        event = Event.objects.get(pk=1)
        user = event.creator
        self.assertEqual(user.id, 1)

    def test_attendees_added_to_event(self):
        # exclude creator from attendees
        test_attendees = User.objects.all().exclude(pk=1)
        event = Event.objects.get(pk=1)

        # add attendees to event
        for attendee in test_attendees:
            event.attendees.add(attendee)

        self.assertEqual(event.attendees.all().count(), 5)

    def test_myEvents_view(self):
        response = self.client.get('/allEvents/')
        # check reponse and template
        self.assertEqual(response.status_code, 200)
        # cehck all events are returned
        self.assertTrue(len(response.context['events']) == 5)
        self.assertTemplateUsed(response, 'html/allEvents.html')

    def test_editEvent_view_(self):
        response = self.client.get('/event/edit/1/')
        # check reponse and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/editEvent.html')
        # check correct event is returned
        correct_event = Event.objects.get(pk=1)
        self.assertEqual(response.context['event'], correct_event)

    def test_search_events(self):
        # Check event search
        response = self.c.post(
            '/event/search/', 
            json.dumps({'event_search': 'Test Event'}),
            'json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        event_search_results = json.loads(response.content)['event_search_results']
        # Check event objs are returned
        self.assertEqual(len(event_search_results), 5)
        # check event objs have values
        for i in range(len(event_search_results)):
            self.assertFalse(event_search_results[i]['id'] == '')
            self.assertFalse(event_search_results[i]['name'] == '')
            self.assertFalse(event_search_results[i]['event_type'] == '')
            self.assertEqual(event_search_results[i]['attendees'], None)

    def test_event_details(self):
        # Check event search
        response = self.c.post(
            '/event/details/', 
            json.dumps({'event_id': 1}),
            'json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        event = json.loads(response.content)['event']

        # Check event obj is returned
        self.assertTrue(event)


class RenderViewsTests(TestCase):

    def test_index_view(self):
        response = self.client.get('')
        # check reponse and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/index.html')

    def test_createEvent_view(self):
        response = self.client.get('/createEvent/')
        # check reponse and template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/createEvent.html')

    def test_allEvents_view(self):
        response = self.client.get('/myEvents/')
        # check redirect for user not signed in
        self.assertEqual(response.status_code, 302)

    def test_signin_view(self):
        response = self.client.get('/signin/')
        # check redirect for user not signed in
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/signin.html')


class AjaxViewsTests(TestCase):
    c = Client()

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='testuser',
            email='testuser@email.com',
            password='password'
        )

    def test_ajax_register_success(self):
        # Check register success
        response = self.c.post('/register/', {
            'register-username': 'testuser1',
            'register-email': 'testuser1@email.com',
            'register-password': 'password'
        })
        self.assertEqual(json.loads(response.content)['status'], 'success')
        self.assertEqual(response.status_code, 200)

    def test_ajax_register_username_in_use(self):
        # Check register failed  username taken
        response = self.c.post('/register/', {
            'register-username': 'testuser',
            'register-email': 'testuser@email.com',
            'register-password': 'password'
        })
        self.assertEqual(json.loads(response.content)['status'], 'fail')
        self.assertEqual(json.loads(response.content)['error_msg'], 'username already in use')

    def test_ajax_register_email_in_use(self):
        # Check register failed email in use
        response = self.c.post('/register/', {
            'register-username': 'testuser1',
            'register-email': 'testuser@email.com',
            'register-password': 'password'
        })
        self.assertEqual(json.loads(response.content)['status'], 'fail')
        self.assertEqual(json.loads(response.content)['error_msg'], 'email already in use')

    def test_ajax_register_password_length(self):
        # Check register failed  password length
        response = self.c.post('/register/', {
            'register-username': 'testuser2',
            'register-email': 'testuser2@email.com',
            'register-password': 'pass'
        })
        self.assertEqual(json.loads(response.content)['status'], 'fail')
        self.assertEqual(json.loads(response.content)['error_msg'], 'password must be atleast 8 characters long')

    def test_ajax_login_fail(self):
        # Check login fail
        response = self.c.post('/login/', {
            'signin-username': 'testuser5000',
            'signin-password': 'password'
        })
        self.assertEqual(json.loads(response.content)['status'], 'fail')
