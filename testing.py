#!/usr/bin/env python

def get_object_and_headers(url):
  if url == 'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags?per_page=100':
    return ([], [
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-0-14',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-0-14',
          u'sha': u'e6a43576772edb2329e07ec940b21a40cd8d7131',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-0-14'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-16',
          u'sha': u'dc7e96dd8e330aeb4035a80b169d6a7ed6d0447a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-17',
          u'sha': u'3abb29bc099fc47f0612f4bfb03719a994862fac',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-18',
          u'sha': u'5e879e65a23236d582953a91eab016ec65608dd3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-19',
          u'sha': u'cd1bf07c7c524954a769e21317f5f5d01e4f97b3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-23',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-23',
          u'sha': u'd53e74b03d7a541dcd152c67c95b8dce0fcbc990',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-23'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-26',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-26',
          u'sha': u'c7beb466292cdd1d225d8b9ac25cf6983a250d1d',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-26'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-1-29',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-1-29',
          u'sha': u'0310580963c7244f9220fd7978d7812061cf2e35',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-29'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-10',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-10',
          u'sha': u'5e4423e5dbe9518bc355c6d6cc9aa75b6f31aed3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-10'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_production-12',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_production-12',
          u'sha': u'1dc03790263ee7f0896a50bb950ed1b4a40ef18e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-12'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-1',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-1',
          u'sha': u'f7a3705102f6e8748e0baa98dd0be26bf4d218e7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-1'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-2',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-2',
          u'sha': u'0364092b78a25349f8d5ff1eb0c02af3a32fcc45',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-2'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-3',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-3',
          u'sha': u'7541d305ceecf3676403be905bd39d2f4ff0fa90',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-3'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-4',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-4',
          u'sha': u'1bac0d2bf5f44e78620d05021c1216cfa215af60',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-4'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-5',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-5',
          u'sha': u'a174f048469141f6b1b484494f49b9ea92bfdeac',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-5'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-6',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-6',
          u'sha': u'1afae60b2fe1b792e47a3c5e63f47a54de5fb633',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-6'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-7',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-7',
          u'sha': u'1bb83e1f7ae33b54434d61ab641153c2cf5ba48c',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-7'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-8',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-8',
          u'sha': u'd429d8367fd9a2e848b0d4b2601cedc1ac357995',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-8'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-9',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-9',
          u'sha': u'06bba48309b10929206c9596196241c85079dd44',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-9'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-10',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-10',
          u'sha': u'b98b9f9b9d682435d53d7793f320ee94d2c9c676',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-10'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-11',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-11',
          u'sha': u'9d0c9d3025951c457d69caef51aaa3ed7677c7ea',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-11'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-12',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-12',
          u'sha': u'27bed01a20eda4ac30b5e5991ba7442de3ed25b7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-12'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-13',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-13',
          u'sha': u'c53dc6fc447cc2ef5fa34df7db736c325b6764d6',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-13'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-14',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-14',
          u'sha': u'bdf6453ab5c5ba3d083b6c0722805a5d528161f6',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-14'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-15',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-15',
          u'sha': u'a03077e07d54c75a1e8b56c1f03a0599455af44f',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-15'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-16',
          u'sha': u'23199733c98ae71cf854e02dbf857ff62618f977',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-17',
          u'sha': u'e0433b671519edf1fe66f9ed032eac51f108f486',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-18',
          u'sha': u'4abdb8d13ef6129e2c730792df1b8ad55156e2d8',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-19',
          u'sha': u'8631a951ad106c884c6d6cdaa8f4924e07674a07',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-20',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-20',
          u'sha': u'3808b3c167375eb7bd32dc7867c25d06826f2d03',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-20'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-21',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-21',
          u'sha': u'886eb91649f10f6e6eb08a9e7e483f1a08ca15e2',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-21'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-22',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-22',
          u'sha': u'364e9204392bbbfb1104f6713cc8858b092ab146',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-22'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-23',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-23',
          u'sha': u'b637ef420b86dc8a8a2f5c2278e443bbd96fcf2d',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-23'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-24',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-24',
          u'sha': u'615c8b439f2731b330e345da9d7610c71780bec7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-24'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-25',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-25',
          u'sha': u'e3be9cac48e02c34fdc0b13148ab163771f2ed53',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-25'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-26',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-26',
          u'sha': u'e59e9604253bedfa6f9af02692e4cd162fea4397',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-26'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-27',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-27',
          u'sha': u'd9ceea563417dd8cfbaf1eedb8c81b30c429e26e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-27'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-28',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-28',
          u'sha': u'859a810a0921ec202e8e68c38cda2bda26fc38c5',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-28'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-29',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-29',
          u'sha': u'675eed63fe0e3c8abeecf978c5fbbb7aaf5c77a2',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-29'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-30',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-30',
          u'sha': u'2f8669515e22c14971a2a98cfdef336762191b78',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-30'
      },

      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-31',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-31',
          u'sha': u'3556693589322324594bcd9f4dd29eb4672ea5de',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-31'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-32',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-32',
          u'sha': u'cabc0b47b5fb78681c315bf83542300d765025d7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-32'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-33',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-33',
          u'sha': u'755306544956a4e96c39a39d1c4aacb3a1dfbd5a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-33'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_release-34',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_release-34',
          u'sha': u'25d5bab9f214500f7520a26091d7d5bcd6385652',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-34'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-0-14',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-0-14',
          u'sha': u'25813c06e419065358a35ee56b340790f0585daf',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-0-14'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-16',
          u'sha': u'8b4540884dd3605f82ecb3395dfb943d4d5dfbcc',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-17',
          u'sha': u'76bcda9d4edd4ae218b7ee9876ab6099a14d89d2',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-18',
          u'sha': u'e3c206e7f734c6c4e8db59e75072f40fa7dc1c91',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-19',
          u'sha': u'd12ab692f46581c76ca8e0d7d65914d1b040ff8f',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-23',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-23',
          u'sha': u'00fb368f0137fe5eeedbf48e8fba007fe810effd',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-23'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-26',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-26',
          u'sha': u'0c74b76503bd398e3cae675521cdab90ba77ddc3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-26'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-29',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-29',
          u'sha': u'85e25a8ce82a4508bb14bd93aa6d387d49f581b9',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-29'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-1-30',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-1-30',
          u'sha': u'85e25a8ce82a4508bb14bd93aa6d387d49f581b9',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-30'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-10',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-10',
          u'sha': u'0243edd4affd0876b7f0a7697c06b0148d07c443',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-10'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/alpha_staging-12',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/alpha_staging-12',
          u'sha': u'34c908fff540dafa5adf797e00160aeeb9f9fe7b',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-12'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-1',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-1',
          u'sha': u'80949ab912f19bc88adacf62c2ca500905914fb1',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-1'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-10',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-10',
          u'sha': u'fa18f0648c2d84cec6bd37ead5091a51c54d803d',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-10'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-12',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-12',
          u'sha': u'e5ea5ac547c31638ac96090290dc79dcc4c06a38',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-12'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-14',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-14',
          u'sha': u'b8e1ac39ef322344e90c36630384ddecd8898641',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-14'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-16',
          u'sha': u'b2b589d30554a507bb8c8c7ea45828440a7fad6e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-17',
          u'sha': u'38fba3e0ed59ce601a41a849bffc7f54f991278e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-18',
          u'sha': u'56ec64d2d04d941fad6371f507f0e5ebbf7a962c',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-19',
          u'sha': u'b643792f73e3a99260ff20b0a88c7ea39cc1b8a9',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-22',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-22',
          u'sha': u'e91d203e2274d6303f3f6e241906cd2eabbde7ef',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-22'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-23',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-23',
          u'sha': u'c76c775b7bf0eef18b6cb3c90a84564d0d2d2a44',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-23'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-24',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-24',
          u'sha': u'76e70ecc70f46bf6da11c806eed4784121bfcd14',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-24'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-25',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-25',
          u'sha': u'4bb295151b23ea8b5447fbef2b603d8becd27401',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-25'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-26',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-26',
          u'sha': u'ecab6f8e835cf9ed6163a807892c5b2543f258f4',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-26'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-27',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-27',
          u'sha': u'ba91cba9bc437dfda3cc717dae7884be1b1b5c81',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-27'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-28',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-28',
          u'sha': u'6c749cc048dbee75406eb6efdb03b3d701c5bc4a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-28'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-29',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-29',
          u'sha': u'56092b5bdbe53eed3602c69d774ab74a43e0c82a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-29'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-30',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-30',
          u'sha': u'ba91cba9bc437dfdb3cc717dae7884be1b1b5c81',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-30'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-31',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-31',
          u'sha': u'17c0e49db9bd716e3af57d1b7d1a417116ee73dc',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-31'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_release-34',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_release-34',
          u'sha': u'17c0e49db9bd716e3af57d1b7d1a417116ee73dc',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-34'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_staging-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_staging-1-16',
          u'sha': u'44f925d33ffa531e94f97391b7fe692fdd66b871',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_staging-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_staging-1-17',
          u'sha': u'e953bbe895d1652953149147221bb91b9bb89ac7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_staging-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_staging-1-19',
          u'sha': u'248a3aa0929b71be95bafb0a00aa1ccb563e732c',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_staging-1-23',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_staging-1-23',
          u'sha': u'462683a88792ac5b26f2786c64a5e0883d273c2a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-23'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_staging-1-26',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_staging-1-26',
          u'sha': u'd4517134edbb0766189294b66dee06595ac4ffde',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-26'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/refs/tags/approved-alpha_staging-1-29',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/approved-alpha_staging-1-29',
          u'sha': u'acd1b0cd0c76412867c7eb961ca54f2d4af54209',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-29'
      }
    ])
  
  elif url.startswith('https://api.github.com/repos/alphagov/pay-frontend/git/tags/'):
    tag = url[len('https://api.github.com/repos/alphagov/pay-frontend/git/tags/'):]
    return ([], 
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/tags/%s' % tag,
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/commits/merge-commit-%s' % tag,
          u'sha': u'aaef30dbe15cddad82ecfab3c9435c440077abe2',
          u'type': u'commit'
        }
      })
      
  elif url.startswith('https://api.github.com/repos/alphagov/pay-frontend/git/commits/merge-commit'):
    fake_sha = url[len('https://api.github.com/repos/alphagov/pay-frontend/git/commits/'):]
    fake_feature_sha = 'feature-commit-%s' % ( url[len('https://api.github.com/repos/alphagov/pay-frontend/git/commits/merge-commit-'):] )
    fake_master_sha = 'master-commit-%s' % ( url[len('https://api.github.com/repos/alphagov/pay-frontend/git/commits/merge-commit-'):] )

    return ([],
      {
        u'author': {
          u'date': u'2016-09-23T15:36:25Z',
          u'name': u'Silvia Mandal\xe0',
          u'email': u'simad@users.noreply.github.com'
        },
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/commits/%s' % fake_sha,
        u'html_url': u'https://github.com/alphagov/pay-frontend/commit/%s' % fake_sha,
        u'sha': fake_sha,
        u'parents': [
          {
            u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/commits/%s' % fake_master_sha,
            u'sha': u'f03198304407e7d0465a423c4c03c03c02b1b7a2',
            u'html_url': u'https://github.com/alphagov/pay-frontend/commit/%s' % fake_master_sha
          },
          {
            u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/commits/%s' % fake_feature_sha,
            u'sha': u'dac8cdac8979f618b002b53d00addc35076b4d5f',
            u'html_url': u'https://github.com/alphagov/pay-frontend/commit/%s' % fake_feature_sha
          }
        ]
      })

  elif url.startswith('https://api.github.com/repos/alphagov/pay-frontend/commits/feature-commit'):
    fake_sha = url[len('https://api.github.com/repos/alphagov/pay-frontend/commits/'):]

    return ([], {
      u'author': {
        u'url': u'https://api.github.com/users/PauloPortugal',
        u'html_url': u'https://github.com/PauloPortugal',
        u'avatar_url': u'https://avatars.githubusercontent.com/u/102318?v=3',
        u'login': u'PauloPortugal',
      },
      u'url': u'https://api.github.com/repos/alphagov/pay-frontend/commits/%s' % fake_sha,
      u'html_url': u'https://github.com/alphagov/pay-frontend/commit/%s' % fake_sha,
      u'sha': fake_sha,
      u'commit': {
        u'author': {
          u'date': u'2016-09-23T14:07:55Z',
          u'name': u'Paulo Monteiro',
          u'email': u'paulo.from.portugal@gmail.com'
        },
        u'url': u'https://api.github.com/repos/alphagov/pay-frontend/git/commits/%s' % fake_sha,
        u'message': 'PP-1023 Fix the stuff'
      }
    })
    
  elif url == 'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags?per_page=100':
    return ([], [

      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_production-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_production-1-16',
          u'sha': u'dc7e96dd8e330aeb4035a80b169d6a7ed6d0447a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_production-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_production-1-17',
          u'sha': u'3abb29bc099fc47f0612f4bfb03719a994862fac',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_production-1-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_production-1-18',
          u'sha': u'5e879e65a23236d582953a91eab016ec65608dd3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_production-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_production-1-19',
          u'sha': u'cd1bf07c7c524954a769e21317f5f5d01e4f97b3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_release-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_release-16',
          u'sha': u'23199733c98ae71cf854e02dbf857ff62618f977',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_release-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_release-17',
          u'sha': u'e0433b671519edf1fe66f9ed032eac51f108f486',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_release-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_release-18',
          u'sha': u'4abdb8d13ef6129e2c730792df1b8ad55156e2d8',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_release-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_release-19',
          u'sha': u'8631a951ad106c884c6d6cdaa8f4924e07674a07',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_staging-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_staging-1-16',
          u'sha': u'8b4540884dd3605f82ecb3395dfb943d4d5dfbcc',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_staging-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_staging-1-17',
          u'sha': u'76bcda9d4edd4ae218b7ee9876ab6099a14d89d2',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_staging-1-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_staging-1-18',
          u'sha': u'e3c206e7f734c6c4e8db59e75072f40fa7dc1c91',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/alpha_staging-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/alpha_staging-1-19',
          u'sha': u'd12ab692f46581c76ca8e0d7d65914d1b040ff8f',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_release-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_release-16',
          u'sha': u'b2b589d30554a507bb8c8c7ea45828440a7fad6e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_release-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_release-17',
          u'sha': u'38fba3e0ed59ce601a41a849bffc7f54f991278e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_release-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_release-18',
          u'sha': u'56ec64d2d04d941fad6371f507f0e5ebbf7a962c',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_release-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_release-19',
          u'sha': u'b643792f73e3a99260ff20b0a88c7ea39cc1b8a9',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_staging-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_staging-1-16',
          u'sha': u'44f925d33ffa531e94f97391b7fe692fdd66b871',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_staging-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_staging-1-17',
          u'sha': u'e953bbe895d1652953149147221bb91b9bb89ac7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/refs/tags/approved-alpha_staging-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/approved-alpha_staging-1-19',
          u'sha': u'248a3aa0929b71be95bafb0a00aa1ccb563e732c',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-19'
      }
    ])
  
  elif url.startswith('https://api.github.com/repos/alphagov/pay-selfservice/git/tags/'):
    tag = url[len('https://api.github.com/repos/alphagov/pay-selfservice/git/tags/'):]
    return ([], 
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/tags/%s' % tag,
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/commits/merge-commit-%s' % tag,
          u'sha': u'aaef30dbe15cddad82ecfab3c9435c440077abe2',
          u'type': u'commit'
        }
      })
      
  elif url.startswith('https://api.github.com/repos/alphagov/pay-selfservice/git/commits/merge-commit'):
    fake_sha = url[len('https://api.github.com/repos/alphagov/pay-selfservice/git/commits/'):]
    fake_feature_sha = 'feature-commit-%s' % ( url[len('https://api.github.com/repos/alphagov/pay-selfservice/git/commits/merge-commit-'):] )
    fake_master_sha = 'master-commit-%s' % ( url[len('https://api.github.com/repos/alphagov/pay-selfservice/git/commits/merge-commit-'):] )

    return ([],
      {
        u'author': {
          u'date': u'2016-09-23T14:39:25Z',
          u'name': u'Silvia Mandal\xe0',
          u'email': u'simad@users.noreply.github.com'
        },
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/commits/%s' % fake_sha,
        u'html_url': u'https://github.com/alphagov/pay-selfservice/commit/%s' % fake_sha,
        u'sha': fake_sha,
        u'parents': [
          {
            u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/commits/%s' % fake_master_sha,
            u'sha': u'f03198304407e7d0465a423c4c03c03c02b1b7a2',
            u'html_url': u'https://github.com/alphagov/pay-selfservice/commit/%s' % fake_master_sha
          },
          {
            u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/commits/%s' % fake_feature_sha,
            u'sha': u'dac8cdac8979f618b002b53d00addc35076b4d5f',
            u'html_url': u'https://github.com/alphagov/pay-selfservice/commit/%s' % fake_feature_sha
          }
        ]
      })

  elif url.startswith('https://api.github.com/repos/alphagov/pay-selfservice/commits/feature-commit'):
    fake_sha = url[len('https://api.github.com/repos/alphagov/pay-selfservice/commits/'):]

    return ([], {
      u'author': {
        u'url': u'https://api.github.com/users/PauloPortugal',
        u'html_url': u'https://github.com/PauloPortugal',
        u'avatar_url': u'https://avatars.githubusercontent.com/u/102318?v=3',
        u'login': u'PauloPortugal',
      },
      u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/commits/%s' % fake_sha,
      u'html_url': u'https://github.com/alphagov/pay-selfservice/commit/%s' % fake_sha,
      u'sha': fake_sha,
      u'commit': {
        u'author': {
          u'date': u'2016-09-24T14:10:55Z',
          u'name': u'Paulo Monteiro',
          u'email': u'paulo.from.portugal@gmail.com'
        },
        u'url': u'https://api.github.com/repos/alphagov/pay-selfservice/git/commits/%s' % fake_sha,
        u'message': 'PP-1023 Fix the stuff'
      }
    })
    
  elif url == 'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags?per_page=100':
    return ([], [

      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_production-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_production-1-16',
          u'sha': u'dc7e96dd8e330aeb4035a80b169d6a7ed6d0447a',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_production-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_production-1-17',
          u'sha': u'3abb29bc099fc47f0612f4bfb03719a994862fac',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_production-1-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_production-1-18',
          u'sha': u'5e879e65a23236d582953a91eab016ec65608dd3',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_production-1-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_release-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_release-16',
          u'sha': u'23199733c98ae71cf854e02dbf857ff62618f977',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_release-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_release-17',
          u'sha': u'e0433b671519edf1fe66f9ed032eac51f108f486',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_release-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_release-18',
          u'sha': u'4abdb8d13ef6129e2c730792df1b8ad55156e2d8',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_release-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_release-19',
          u'sha': u'8631a951ad106c884c6d6cdaa8f4924e07674a07',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_release-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_staging-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_staging-1-16',
          u'sha': u'8b4540884dd3605f82ecb3395dfb943d4d5dfbcc',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_staging-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_staging-1-17',
          u'sha': u'76bcda9d4edd4ae218b7ee9876ab6099a14d89d2',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_staging-1-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_staging-1-18',
          u'sha': u'e3c206e7f734c6c4e8db59e75072f40fa7dc1c91',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/alpha_staging-1-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/alpha_staging-1-19',
          u'sha': u'd12ab692f46581c76ca8e0d7d65914d1b040ff8f',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/alpha_staging-1-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/approved-alpha_release-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/approved-alpha_release-16',
          u'sha': u'b2b589d30554a507bb8c8c7ea45828440a7fad6e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/approved-alpha_release-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/approved-alpha_release-17',
          u'sha': u'38fba3e0ed59ce601a41a849bffc7f54f991278e',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-17'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/approved-alpha_release-18',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/approved-alpha_release-18',
          u'sha': u'56ec64d2d04d941fad6371f507f0e5ebbf7a962c',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-18'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/approved-alpha_release-19',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/approved-alpha_release-19',
          u'sha': u'b643792f73e3a99260ff20b0a88c7ea39cc1b8a9',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_release-19'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/approved-alpha_staging-1-16',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/approved-alpha_staging-1-16',
          u'sha': u'44f925d33ffa531e94f97391b7fe692fdd66b871',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-16'
      },
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/refs/tags/approved-alpha_staging-1-17',
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/approved-alpha_staging-1-17',
          u'sha': u'e953bbe895d1652953149147221bb91b9bb89ac7',
          u'type': u'tag'
        }, 
        u'ref': u'refs/tags/approved-alpha_staging-1-17'
      }
    ])
  
  elif url.startswith('https://api.github.com/repos/alphagov/pay-connector/git/tags/'):
    tag = url[len('https://api.github.com/repos/alphagov/pay-connector/git/tags/'):]
    return ([], 
      {
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/tags/%s' % tag,
        u'object': {
          u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/commits/merge-commit-%s' % tag,
          u'sha': u'aaef30dbe15cddad82ecfab3c9435c440077abe2',
          u'type': u'commit'
        }
      })
      
  elif url.startswith('https://api.github.com/repos/alphagov/pay-connector/git/commits/merge-commit'):
    fake_sha = url[len('https://api.github.com/repos/alphagov/pay-connector/git/commits/'):]
    fake_feature_sha = 'feature-commit-%s' % ( url[len('https://api.github.com/repos/alphagov/pay-connector/git/commits/merge-commit-'):] )
    fake_master_sha = 'master-commit-%s' % ( url[len('https://api.github.com/repos/alphagov/pay-connector/git/commits/merge-commit-'):] )

    return ([],
      {
        u'author': {
          u'date': u'2016-09-26T09:10:25Z',
          u'name': u'Silvia Mandal\xe0',
          u'email': u'simad@users.noreply.github.com'
        },
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/commits/%s' % fake_sha,
        u'html_url': u'https://github.com/alphagov/pay-connector/commit/%s' % fake_sha,
        u'sha': fake_sha,
        u'parents': [
          {
            u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/commits/%s' % fake_master_sha,
            u'sha': u'f03198304407e7d0465a423c4c03c03c02b1b7a2',
            u'html_url': u'https://github.com/alphagov/pay-connector/commit/%s' % fake_master_sha
          },
          {
            u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/commits/%s' % fake_feature_sha,
            u'sha': u'dac8cdac8979f618b002b53d00addc35076b4d5f',
            u'html_url': u'https://github.com/alphagov/pay-connector/commit/%s' % fake_feature_sha
          }
        ]
      })

  elif url.startswith('https://api.github.com/repos/alphagov/pay-connector/commits/feature-commit'):
    fake_sha = url[len('https://api.github.com/repos/alphagov/pay-connector/commits/'):]

    return ([], {
      u'author': {
        u'url': u'https://api.github.com/users/PauloPortugal',
        u'html_url': u'https://github.com/PauloPortugal',
        u'avatar_url': u'https://avatars.githubusercontent.com/u/102318?v=3',
        u'login': u'PauloPortugal',
      },
      u'url': u'https://api.github.com/repos/alphagov/pay-connector/commits/%s' % fake_sha,
      u'html_url': u'https://github.com/alphagov/pay-connector/commit/%s' % fake_sha,
      u'sha': fake_sha,
      u'commit': {
        u'author': {
          u'date': u'2016-09-24T14:10:55Z',
          u'name': u'Paulo Monteiro',
          u'email': u'paulo.from.portugal@gmail.com'
        },
        u'url': u'https://api.github.com/repos/alphagov/pay-connector/git/commits/%s' % fake_sha,
        u'message': 'PP-1023 Fix the stuff'
      }
    })
    
  elif url.startswith('https://api.github.com/repos/alphagov/pay-') and url.endswith('/git/refs/tags?per_page=100'):
    return ([], [])


  
  raise Exception(url)
