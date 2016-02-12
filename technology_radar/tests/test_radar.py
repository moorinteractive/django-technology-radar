import pytest

from django.core.urlresolvers import reverse

from technology_radar.tests.factories import (
    AreaFactory, StatusFactory, RadarFactory, BlipFactory)


@pytest.mark.django_db
def test_area():
    radar = AreaFactory()
    assert str(radar) == 'Tools'


@pytest.mark.django_db
def test_status():
    radar = StatusFactory()
    assert str(radar) == 'Access'


@pytest.mark.django_db
def test_radar():
    radar = RadarFactory()
    assert str(radar) == 'Moor Interactive'


@pytest.mark.django_db
def test_blip():
    blip = BlipFactory()
    assert str(blip) == 'BEM'


@pytest.mark.django_db
def test_api_radar_list(client):
    res = client.get(reverse('api-radar-list'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_api_radar_detail(client):
    radar = RadarFactory()
    res = client.get(reverse('api-radar-detail', kwargs={
        'pk': 1
    }))
    assert res.status_code == 200
    res = client.get(reverse('api-radar-detail', kwargs={
        'pk': 2
    }))
    assert res.status_code == 404


@pytest.mark.django_db
def test_api_blip_list(client):
    res = client.get(reverse('api-blip-list'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_api_blip_detail(client):
    blip = BlipFactory()
    res = client.get(reverse('api-blip-detail', kwargs={
        'pk': 1
    }))
    assert res.status_code == 200
    res = client.get(reverse('api-blip-detail', kwargs={
        'pk': 2
    }))
    assert res.status_code == 404


@pytest.mark.django_db
def test_index(client):
    res = client.get(reverse('index'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_radar_detail(client):
    radar = RadarFactory()
    res = client.get(reverse('radar-detail', kwargs={
        'radar': 'moor-interactive'
    }))
    assert res.status_code == 200
    res = client.get(reverse('radar-detail', kwargs={
        'radar': 'moor-interactiv'
    }))
    assert res.status_code == 404


@pytest.mark.django_db
def test_area_detail(client):
    blip = BlipFactory()
    res = client.get(reverse('area-detail', kwargs={
        'radar': 'moor-interactive',
        'area': 'tools'
    }))
    assert res.status_code == 200
    res = client.get(reverse('area-detail', kwargs={
        'radar': 'moor-interactiv',
        'area': 'tools'
    }))
    assert res.status_code == 404
    res = client.get(reverse('area-detail', kwargs={
        'radar': 'moor-interactive',
        'area': 'tool'
    }))
    assert res.status_code == 404


@pytest.mark.django_db
def test_blip_detail(client):
    blip = BlipFactory()
    res = client.get(reverse('blip-detail', kwargs={
        'radar': 'moor-interactive',
        'area': 'tools',
        'blip': 'bem'
    }))
    assert res.status_code == 200
    res = client.get(reverse('blip-detail', kwargs={
        'radar': 'moor-interactive',
        'area': 'tools',
        'blip': 'be'
    }))
    assert res.status_code == 404
    radar = RadarFactory(name='Company')
    res = client.get(reverse('blip-detail', kwargs={
        'radar': 'company',
        'area': 'tools',
        'blip': 'bem'
    }))
    assert res.status_code == 404
