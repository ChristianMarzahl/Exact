import {TestBed} from '@angular/core/testing';

import {TeamService} from './team.service';
import {HttpCachingInterceptor} from '../../interceptors/caching-http.service';
import {MockCachingHttpClient} from '../../interceptors/caching-http.service.spec';
import {Team} from '../../types/team';

describe('TeamService', () => {
    const testTeams: Team<any>[] = [{
        id: 0,
        website: 'https://website',
        name: 'AwesomeTeam1',
        members: [0, 1],
        admins: [0],
        permissions: {
            userManagement: false,
            manageExportFormats: true,
            createSet: true
        }
    }];

    beforeEach(() => TestBed.configureTestingModule({
        providers: [
            {provide: HttpCachingInterceptor, useClass: MockCachingHttpClient}
        ]
    }));

    it('should be created', () => {
        const service: TeamService = TestBed.get(TeamService);
        expect(service).toBeTruthy();
    });

    it('should return correct get() result', (done) => {
        const service: TeamService = TestBed.get(TeamService);
        const httpClient: MockCachingHttpClient = TestBed.get(HttpCachingInterceptor);

        httpClient.responses[`${service.url}${testTeams[0].id}/`] = testTeams[0];

        service.get(testTeams[0].id).subscribe(result => {
            expect(result).toBe(testTeams[0]);
            done();
        });
    });
});
