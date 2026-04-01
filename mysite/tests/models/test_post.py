import pytest

from blog.models.factories import PostFactory

@pytest.fixture
def post_publisehd():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_publisehd):
    assert post_publisehd.title == 'pytest with factory'