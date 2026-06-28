from django.test import TestCase
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Contract


class ContractModelTests(TestCase):
    def test_contract_table_uses_contact_form_fields(self):
        self.assertEqual(Contract._meta.db_table, 'contract')

        field_names = {
            field.name
            for field in Contract._meta.fields
            if field.name != 'id'
        }

        self.assertEqual(
            field_names,
            {'name', 'email', 'whatsapp', 'requirement'},
        )


class ContractApiTests(TestCase):
    def test_post_creates_contract_form_record(self):
        response = self.client.post(
            '/api/contract/',
            data={
                'name': 'Maya Buyer',
                'email': 'maya@example.com',
                'whatsapp': '+91 98765 43210',
                'requirement': 'Need pearl beaded evening bags for bridal retail.',
            },
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Contract.objects.count(), 1)

        contract = Contract.objects.get()
        self.assertEqual(contract.name, 'Maya Buyer')
        self.assertEqual(contract.email, 'maya@example.com')
        self.assertEqual(contract.whatsapp, '+91 98765 43210')
        self.assertEqual(contract.requirement, 'Need pearl beaded evening bags for bridal retail.')
        self.assertEqual(
            response.json(),
            {
                'id': contract.id,
                'name': 'Maya Buyer',
                'email': 'maya@example.com',
                'whatsapp': '+91 98765 43210',
                'requirement': 'Need pearl beaded evening bags for bridal retail.',
            },
        )

    def test_post_requires_all_contract_form_fields(self):
        response = self.client.post(
            '/api/contract/',
            data={
                'name': 'Maya Buyer',
                'email': 'maya@example.com',
            },
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Contract.objects.count(), 0)
        self.assertEqual(
            response.json(),
            {
                'errors': {
                    'whatsapp': 'This field is required.',
                    'requirement': 'This field is required.',
                },
            },
        )

    def test_returns_latest_contract_form_record(self):
        Contract.objects.create(
            name='Old Buyer',
            email='old@example.com',
            whatsapp='+91 11111 11111',
            requirement='Old requirement',
        )
        Contract.objects.create(
            name='Andy',
            email='andy@example.com',
            whatsapp='+86 13800000000',
            requirement='Need hand beaded bags',
        )

        response = self.client.get('/api/contract/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                'name': 'Andy',
                'email': 'andy@example.com',
                'whatsapp': '+86 13800000000',
                'requirement': 'Need hand beaded bags',
            },
        )


class ContractAdminTests(TestCase):
    def test_contract_is_registered_in_admin(self):
        self.assertIn(Contract, admin.site._registry)

    def test_contract_admin_lists_real_database_records(self):
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password123',
        )
        self.client.force_login(admin_user)
        Contract.objects.create(
            name='Lisa',
            email='lisa@hotmail.com',
            whatsapp='9779704417273',
            requirement='Very excited to get your product',
        )

        response = self.client.get(reverse('admin:website_contract_changelist'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lisa')
        self.assertContains(response, 'lisa@hotmail.com')
        self.assertContains(response, '9779704417273')
