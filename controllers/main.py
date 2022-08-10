from odoo import http
from odoo.http import request


class ELearning(http.Controller):
    @http.route(['/elearning/snippet'], type="json", auth="public")
    def elearning_snippet(self):
        course_obj = request.env['slide.channel'].sudo().search(
            [], order='create_date DESC', limit=3)
        li = []
        for item in course_obj:
            vals = {"courses": item.name,
                    "promote_strategy": item.promote_strategy,
                    "description": item.description_short
                    }
            li.append(vals)
        return li
        # print(li)
        # li = []
        # for item in course_obj:
        #     print(item)
        #     li.append(item)
        #     vals = {"courses": item.name}
        # print(li)
        # return json_string
    @http.route(['/course1'], type='http', auth='public',
                website=True)
    def click(self, **post):
        # id = post['course1']
        return request.redirect(
            "slides/"+str(1))
    