from odoo import http
from odoo.http import request


class ELearning(http.Controller):
    @http.route(['/elearning/snippet'], type="json", auth="public")
    def elearning_snippet(self):
        course_obj = request.env['slide.channel'].sudo().search(
            [], order='create_date DESC', limit=3)

        # course_id=request.env['slide.channel'].sudo().search([])
        # li = []
        # for item in course_obj:
        # name=item.name
        vals = {"courses": course_obj}
        response = http.Response(template='elearning_snippet.custom_snippets',
                                 qcontext=vals)
        return response.render()
        # li.append(vals)
        # print(li)
        # print(vals)
        # return vals

        # last working
        # li = []
        # for item in course_obj:
        #     print(item)
        #     # name = item.name
        #     course1 = {"course_name": item.name,
        #                "course_id": item.id,
        #                "promote_strategy": item.promote_strategy,
        #                "description": item.description_short
        #                }
        #     li.append(course1)
        # print(li)
        # return li

    # @http.route(['/course1'], type='http', auth='public',
    #             website=True)
    # def click(self, **post):
    #     # id = post['course1']
    #     return request.redirect(
    #         "slides/"+str(1))
